from urllib.parse import urlparse

url = "http://devops.pipixia.run/TaskCenter/versionModify";
uc = urlparse(url);
print("URL: ", uc.netloc)
