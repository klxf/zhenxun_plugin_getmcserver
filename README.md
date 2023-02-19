# zhenxun_plugin_getmcserver
一个很简单的获取服务器在线人数、玩家列表的插件

## 开始使用
### 安装
在 Releases 下载到最新的 `.zip` 压缩包，解压到真寻的 `extensive_plugin` 目录
### 配置
在 `data` 目录下新建 `get_mcserver` 文件夹，新建 `群号.json`

| 键            | 值    | 描述        |
|--------------|------|-----------|
| server_name  | 字符串  | 服务器名称     |
| ip           | 字符串  | 服务器IP     |
| port         | 字符串  | 服务器端口     |
| playerlist   | 布尔值  | 是否显示玩家列表  |

例如：
```json
{
  "server_name": "Test",
  "ip": "127.0.0.1",
  "port": "25565",
  "playerlist": true
}
```
### 命令
只在群聊中生效：`gets`