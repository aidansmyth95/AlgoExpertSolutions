'''
Very close to youngest common ancestor, only data struct is different.
Solving can be done really well with recursion.
If two direct reports in a subtree have common manager.
Recursively calculate sum of direct reports in subtree, whichever has num is
the correct node.
'''

# O(n) T | O(d) S
def getLowestCommonManager(topManager, reportOne, reportTwo):
	# helper method returning instance of org info class
    return getOrgInfo(topManager, reportOne, reportTwo).lowestCommonManager

def getOrgInfo(manager, reportOne, reportTwo):
	# rooted at this "manager"
	numImportantReports = 0
	for directReport in manager.directReports:
		# call for each direct report
		orgInfo = getOrgInfo(directReport, reportOne, reportTwo)
		if orgInfo.lowestCommonManager is not None:
			# check if we had a LCM found, we are done. Return orgInfo.
			return orgInfo
		# increment the number of important reports
		numImportantReports += orgInfo.numImportantReports
	if manager == reportOne or manager == reportTwo:
		# if manager is the direct report, increment found reports
		numImportantReports += 1
	# LCM only not None is both important reports have been found
	lowestCommonManager = manager if numImportantReports == 2 else None
	# return class with new info
	return OrgInfo(lowestCommonManager, numImportantReports)
		
# define interface for org info
class OrgInfo:
	def __init__(self, lowestCommonManager, numImportantReports):
		self.lowestCommonManager = lowestCommonManager
		self.numImportantReports = numImportantReports

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
