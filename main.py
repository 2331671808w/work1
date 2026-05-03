from core.npc import NPC

if __name__ == "__main__":
    npc = NPC("莉亚")

    print("NPC 已启动（输入 exit 退出）")

    while True:
        player_input = input("你：")
        if player_input == "exit":
            break

        reply = npc.respond(player_input)
        print("NPC：", reply)
