import json

file = "updaterequest.json"

with open(file, "r") as json_file:
    update = json.load(json_file) #dict

#update keys: 'updateType', 'type', 'agent', 'agentVersion', 'pluginVersion', 'orgToken', 'userKey', 'product', 'productVersion', 'timeStamp', 'requesterEmail', 'projects', 'aggregateModules', 'preserveModuleStructure', 'aggregateProjectName', 'aggregateProjectToken', 'logData', 'scanComment', 'extraProperties', 'scanSummaryInfo', 'contributions'

try:
    updateType = update["updateType"]
    print(f"Update type: {updateType}")

    agent = update["agent"]
    print(f"Agent used: {agent}")

    plugin = update["pluginVersion"]
    print(f"UA Version used: {plugin}")

    orgToken = update["orgToken"]
    userKey = update["userKey"]
    product = update["product"]
    timeStamp = update["timeStamp"]

    email = update["requesterEmail"]
    print(f"Email: {email}\nTime: {timeStamp}")
except KeyError:
    pass

checkLen = len(update["projects"])
if checkLen > 1:
    print(f"There are {checkLen} projects in this request. 'projects' is hard-coded to 0.")
elif checkLen == 1:
    pass
else:
    print("something is fucked up here...")
    quit

projects = update["projects"] #list
projects[0]
#projects keys: 'coordinates', 'dependencies', 'projectToken', 'projectSetupStatus', 'projectTags'
dependencies = projects[0]["dependencies"] #list
dep_length = 2 #len(dependencies)

x = 3
one_dependency = dependencies[x] #dict
#one_dependency keys: 'artifactId', 'sha1', 'otherPlatformSha1', 'systemPath', 'optional', 'children', 'exclusions', 'licenses', 'copyrights', 'filename', 'checksums', 'aggregatedDependencies'
#should also have 'dependencyFile'

file_count = 0
for y in dependencies:
    if y.get("children") == None:
        print(y["filename"] + " has no children. \nDependency file: ")
        file_count += 1
        try:
            print("\t\t" + y["dependencyFile"] + "\n")
        except:
            KeyError
    elif len(y["children"]) == 0:
        print(y["filename"] + " has no children. \n Dependency file: ")
        file_count += 1
        try:
            print("\t\t" + y["dependencyFile"] + "\n")
        except:
            KeyError
    else:
        print(y["filename"] + " has children.\n\tDependency file: \n")
        file_count += 1
        try:
            print("\t\t" + y["dependencyFile"] + "\n")
        except:
            KeyError
        a = 0
        while a < len(y["children"]):
            print("\t-- " + y["children"][a]["filename"])
            a += 1
            file_count += 1
            
print(file_count)
   
#'children' is a list, maybe length? if empty, it is zero.
#'children' keys: 'groupId', 'artifactId', 'version', 'type', 'scope', 'sha1', 'systemPath', 'optional', 'children', 'filename', 'dependencyType', 'checksums', 'dependencyFile', 'additionalSha1', 'deduped'
#print(one_dependency['children'][0]['filename'])

scansummaryinfo = update["scanSummaryInfo"] #dict
#keys: 'totalElapsedTime', 'stepsSummaryInfo', 'packageManagers', 'sourceControlManagers', 'containerRegistries', 'otherIntegrationTypes', 'isPrivileged', 'scanMethod', 'scanStatistics'
steps = scansummaryinfo["stepsSummaryInfo"] #list
steps_len = len(steps)
try:
    packagemanagers = scansummaryinfo["packageManagers"]
    stepFetch = steps[0]["stepCompletionStatus"]
    deps_count = steps[1]["totalUniqueDependenciesFound"]
    fetch = steps[0]["stepName"]
    stepName = steps[1]["stepName"]
    stepStatus = steps[1]["stepCompletionStatus"]
    sources = steps[2]["totalSourceBinariesFound"]
    filescan = steps[2]["stepName"]
    filescanstatus = steps[2]["stepCompletionStatus"]
    print(f"Package manager(s) detected: {packagemanagers}")
    print(f"Total Unique Dependencies found: {deps_count}")
    print(f"Step name: {fetch}\n\t Status: {stepFetch}")
    print(f"Step name: {stepName}\n\t Status: {stepStatus}")
    print(f"Step name: {filescan}\n\t Status: {filescanstatus}\n\t Source files/binaries found count: {sources}")
except:
    KeyError
