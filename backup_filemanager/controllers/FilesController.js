import dbClient from '../utils/db';
import redisClient from '../utils/redis';
import { v4 } from 'uuid';
const fs = require('fs').promises;
const { promisify } = require('util');
const mkdirp = require('mkdirp');
const { ObjectID } = require('mongodb');
const path = process.env.FOLDER_PATH || '/tmp/files_manager';

/**
 * Contains files miscellanous handlers
 */
class FilesController {
	static async postUpload(req, res) {
		const x_tok = req.headers['x-token'];
		if (!x_tok) { res.json(); return;}
		const usr_id = await redisClient.get(`auth_${x_tok}`);
		if (!usr_id) {
			res.status(401).json({"error": "Unauthorized"});
			return;
		}
		const user = await (await dbClient.client.db().collection('users'))
		.findOne({ "_id": ObjectID(usr_id) });
		if (!user) { 
			res.status(401).json({"error": "Unauthorized"});
			return;
		}
		if (!req.body) { res.json(); return; }
		const name = req.body.name || null;
		const type = req.body.type || null;
		const parentId = req.body.parentId || 0;
		const isPublic = req.body.isPublic || false;
		let data = null;
		if (type && (type === 'file' || type === 'image')) { 
			data = req.body.data || null; }
		if (!name) {
			res.status(400).json({"error": "Missing name"});
			return;
		}
		if (!type) {
			res.status(400).json({"error": "Missing type"});
			return;
		}
		if (((type === 'image') || (type === 'file')) && !data) {
			res.status(400).json({"error": "Missing data"});
			return;
		}
		if (req.body.parentId === 0) {
			const file = await (await dbClient.client.db().collection('files'))
			.findOne({ "parentId": parentId.toString() });
			if (!file) {
				res.status(400).json({"error": "Parent not found"});
				return;
			}
			if (file.type !== 'folder') {
				res.status(400).json({"error": "Parent is not a folder"});
				return;
			}
		}
		if (type === 'folder' && name) {
			const saved_folder = await (await dbClient.client.db().collection('files'))
			.insertOne({ "user_Id": ObjectID(usr_id), "name": name,
			"type": type, "parentId": parentId.toString(), "isPublic": isPublic });

			res.status(201).json({"id": saved_folder.insertedId.toString(),
				"userId": usr_id, "name": name, "type": type,
				"isPublic": isPublic, "parentId": parentId });
			return;
		}
		const newFileName = v4();

		//Function to check if directory exists and creates it async
		const createDir = () => { return fs.mkdir(path, {recursive: true}); };

		//function to create file with name as uuid4 created and write to it async
		const writeInFile = async () => {
			try {
				await createDir();
				await fs.writeFile(`${path}/${newFileName}`, Buffer.from(data, 'base64'));
			}
			catch {
				console.log('Error writing file');
			}
		};
		// calling the function for doing both create dir and file writing
		await writeInFile();
		const saved_file = await (await dbClient.client.db().collection('files'))
			.insertOne({ "user_Id": ObjectID(usr_id), "name": name,
			"type": type, "parentId": parentId.toString(), "isPublic": isPublic,
			"localPath": path + '/' + newFileName });
		res.status(201).json({"id": saved_file.insertedId.toString(),
				"userId": usr_id, "name": name, "type": type,
				"isPublic": isPublic, "parentId": parentId });
		return;
	}

	static async getShow(req, res) {
		const x_tok = req.headers['x-token'];
		if (!x_tok) { res.json(); return;}
		const usr_id = await redisClient.get(`auth_${x_tok}`);
		if (!usr_id) {
			res.status(401).json({"error": "Unauthorized"});
			return;
		}
		const user = await (await dbClient.client.db().collection('users'))
		.findOne({ "_id": ObjectID(usr_id) });
		if (!user) { 
			res.status(401).json({"error": "Unauthorized"});
			return;
		}
		const file_id = req.params.id;
		const file = await (await dbClient.client.db().collection('files'))
		.findOne({ "user_Id": ObjectID(usr_id), "_id": ObjectID(file_id) });
		if (!file) {
			res.status(404).json({"error": "Not found"});
			return;
		}
		res.status().json({"id": file._id, "userId": file.userId, "name": file.name,
			"type": file.type, "isPublic": file.isPublic, "parentId": file.parentId});
		return;
	}
}

export default FilesController;
module.exports = FilesController;