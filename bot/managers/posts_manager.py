from main import vk, config

async def __get_ready_post_params(data: dict, post_config: dict) -> dict:
	return {
		"owner_id": -config.group_id,
		"attachments": post_config["attachments"],
		"message": post_config["post"].format(banned = data["banned"], by = data["by"], reason = data["reason"])
	}

async def create_post(data: dict) -> int:
	params = await __get_ready_post_params(data, config.post_templates["waiting"])
	response = await vk.send_api_request("wall.post", params)
	return response["post_id"]

async def edit_post(status: str, data: dict):
	params = await __get_ready_post_params(data, config.post_templates[status]) | {"post_id": data["vk_post"]}
	await vk.send_api_request("wall.edit", params)