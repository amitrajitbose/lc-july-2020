class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minuteAngle = (minutes/60) * 360
        hourAngle = ((hour/12) * 360) + ((minutes/60) * 30)
        diff = abs(hourAngle-minuteAngle)
        return min(diff, 360-diff)

