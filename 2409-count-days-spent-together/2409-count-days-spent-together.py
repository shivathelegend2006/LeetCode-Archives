class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        
        def dayNum(mmdd):
            m,d = map(int, mmdd.split("-"))

            months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            days = {
                1: 0,
                2: 31,
                3: sum(months[0:2]),
                4: sum(months[0:3]),
                5: sum(months[0:4]),
                6: sum(months[0:5]),
                7: sum(months[0:6]),
                8: sum(months[0:7]),
                9: sum(months[0:8]),
                10: sum(months[0:9]),
                11: sum(months[0:10]),
                12: sum(months[0:11])
            }
            return days[m] + d

        aa = dayNum(arriveAlice)
        la = dayNum(leaveAlice)

        ab = dayNum(arriveBob)
        lb = dayNum(leaveBob)
        if (la < ab) or (lb < aa): return 0
        print(aa,ab,la,lb)
        return min(la,lb) - max(aa,ab) + 1