from automator import Automator
from target import TargetType

if __name__ == '__main__':
    # 声明货物要移动到的位置，注意根据实际情况调整，没摆出来的建筑可以注释掉
    """
    编号对应位置如下
    7 8 9
    4 5 6
    1 2 3
    """
    targets = {
        # TargetType.Chair: 1,
        # TargetType.Wood: 7,
        # TargetType.Bottle: 4,
        # TargetType.Vegetable: 5,
        # TargetType.Box: 1,
        # TargetType.Food: 8,
        # TargetType.Book: 6,
        # TargetType.Coal: 9,
        # TargetType.Grass: 8,
        # TargetType.Bag: 5,
        # TargetType.Sofa: 2,
        TargetType.Chicken: 6,
        TargetType.Carpet:2,
        TargetType.Microphone:5,
        TargetType.Oil:8,
        TargetType.Tool:7,
        # TargetType.Dogfood:1,
        # TargetType.Shoes:4,
        # TargetType.Armoire:3
        # TargetType.Plant: 3,
        # TargetType.Cloth:5,
        # TargetType.Cotton:8,
        # TargetType.Stone:7
    }

    # 脚本模式---拉货，福气，多福，相册
    mode = '相册'
    # 连接 adb 。
    instance = Automator('127.0.0.1:7555', targets,mode)

    # 启动脚本。
    instance.start()
