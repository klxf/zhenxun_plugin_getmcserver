from configs.path_config import DATA_PATH
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
from nonebot.rule import to_me
import json
import requests


__zx_plugin_name__ = "获取MC服务器信息"
__plugin_usage__ = """
usage：
    获取与群聊绑定的MC服务器信息
    指令：
        gets
""".strip()
__plugin_des__ = "获取与群聊绑定的MC服务器信息"
__plugin_cmd__ = ["gets"]
__plugin_version__ = 0.1
__plugin_author__ = "Mr_Fang"
__plugin_settings__ = {
    "level": 5,
    "default_status": False,
    "limit_superuser": False,
    "cmd": ["gets"],
}

getserver = on_command("gets", priority=5, block=True, rule=to_me())


@getserver.handle()
async def _(event: GroupMessageEvent):
    filename = str(event.group_id) + ".json"
    group_config_json = (DATA_PATH / "get_mcserver" / filename)
    if group_config_json.exists():
        config = json.loads(open(group_config_json, "r").read())
        url = "https://api.miri.site/mcPlayer/get.php?ip=" + config["ip"] + "&port=" + config["port"]
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.content)
            if "error" not in data:
                msg = "服务器 " + config["server_name"] + " 数据已请求完毕\n"
                msg += "在线人数：" + str(data["online"]) + "/" + str(data["max"]) + "\n"
                if config["playerlist"]:
                    msg += "在线玩家：\n"
                    for i in range(0, len(data["sample"])):
                        msg += data["sample"][i]["name"] + "\n"
            else:
                msg = "【Error】" + data["error"]
        else:
            msg = "【Error】无法请求 API，请联系开发者"
    else:
        msg = "本群未绑定任何服务器"
    await getserver.send(msg)