from target import TargetType
from cv import UIMatcher
import uiautomator2 as u2
from datetime import datetime,timedelta
import time



class Automator:
    def __init__(self, device: str, targets: dict,ban_list:list):
        # device: 如果是 USB 连接，则为 adb devices 的返回结果；如果是模拟器，则为模拟器的控制 URL 。
        self.d = u2.connect(device)
        self.targets = targets
        self.positions = {
            1: (294, 1184),
            2: (551, 1061),
            3: (807, 961),
            4: (275, 935),
            5: (535, 810),
            6: (799, 687),
            7: (304, 681),
            8: (541, 568),
            9: (787, 447)
        }
        self.ban_list = ban_list

    def start(self):
        sleep_time = 3      #两次检测之间的间隔
        no_train_counter = 0        #连续没有检测到火车的次数
        while True:
            # 判断是否出现货物。
            Screen = self.d.screenshot(format="opencv")
            self.d.click(550, 1650)

            # 滑动屏幕，收割金币。
            self._swipe()
            if UIMatcher.Detect_signal_object(Screen, 'Train.jpg'):
                print('火车来了！')
                no_train_counter = 0
                success_counter = 0 
                time.sleep(2)       #确保火车停了下来
                screen = self.d.screenshot(format="opencv")
                for target in TargetType:
                    if success_counter > 2:
                        print('成功找到3个货物，提前结束！')
                        break
                    if self._match_target(target,screen):
                        success_counter += 1
                        if target in self.ban_list:
                            print(f'遇到{target.value[8:-4]}重启游戏...')
                            self.d.app_stop("com.tencent.jgm")
                            self.d.app_start("com.tencent.jgm")
                            time.sleep(10)


            else:
                no_train_counter+=1
                if no_train_counter>=20:
                    print(f'连续{no_train_counter*sleep_time}s没有检测到火车,sleep_time变为{5*60}s')
                    sleep_time = 5*60
            time.sleep(sleep_time)



    def _swipe(self):
        # 滑动屏幕，收割金币。
        for i in range(3):
            # 横向滑动，共 3 次。
            sx, sy = self._get_position(i * 3 + 1)
            ex, ey = self._get_position(i * 3 + 3)
            self.d.swipe(sx, sy, ex, ey)

    def _get_position(self,key):
        # 获取指定建筑的屏幕位置。
        return self.positions.get(key)

    def _get_target_position(self, target: TargetType):
        # 获取货物要移动到的屏幕位置。
        return self._get_position(self.targets.get(target))

    def _match_target(self, target: TargetType,screen):
        # 探测货物，并搬运货物。

        result = UIMatcher.match(screen, target)
        if result is not None:
            sx, sy = result
            # 获取货物目的地的屏幕位置。
            ex, ey = self._get_target_position(target)

            # 搬运货物。
            if target not in self.ban_list:
                for j in range(3):
                    self.d.swipe(sx, sy, ex, ey)
            return True
        return False


