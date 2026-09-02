class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #brillian brikliant brillaint algo called
        #floyd tortoise and hare

        tort, hare = 0, 0
        while True:
            tort = nums[tort] # one step at a time
            hare = nums[nums[hare]] # two steps at a time
            if hare == tort: break
        #tort is now standing n steps from the entrnce of the loop
        #loop is the place of dulciate
        #we send another tort to now move from start as 
        #dist form start to entrance is the same dist left for inner tort
        tort2 = 0
        while tort != tort2:
            tort = nums[tort]
            tort2 = nums[tort2]

        return tort