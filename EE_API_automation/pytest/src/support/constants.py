import datetime, requests, os, jmespath

test_on_prod = True

class launch_details:
    if test_on_prod:
        userid_primary = 'YOUR OSIO USER ID'  ####  ENTER YOUR OSIO USER ID HERE
        base_url = r"https://api.openshift.io"
    else:
        userid_primary = 'testuser'
        userid_secondary = 'testuser2'
        base_url = r"http://192.168.42.211:30000"
    
    def __init__(self):
        self.space_name = self.create_space_name()
        if test_on_prod:
            self.token_userid_primary = "YOUR OSIO SECURITY TOKEN"  ####  ENTER YOUR OSIO SECURITY TOKEN HERE
        else:
            self.token_userid_primary = self.get_keycloak_token()
        

    def get_keycloak_token(self):
        url = self.create_url('api/login/generate')
        r = requests.get(url)
        return self.extract_value("[0].token.access_token", r)
    
    def create_space_name(self):
        var = datetime.datetime.now()
        var = var.isoformat().rsplit('.')[0]
        space = self.userid_primary + "-space-" + var
        print "Space Name = ", space
        return space
    
    def create_url(self, api):
        return os.path.join(self.base_url, api)

    def extract_value(self, extract_path=None, json_response=None):
        if None in [json_response, extract_path]:
            print "Either Jason response or the extractor path are None"
            return None
        else:
            try:
                return jmespath.search(extract_path, json_response.json())
            except:
                print "Exception extracting value from the response body"
                return None
launch_detail = launch_details()
 
class requests_constants:
    base_url_default = r'https://api.openshift.io'
    content_type_key_default = 'Content-Type'
    content_type_default = r'application/vnd.api+json'
    content_header_default = {'Content-Type': 'application/vnd.api+json'}
    authorization_key_default = 'Authorization'
    authorization_carrier_default = 'Bearer '
    headers_default = {content_type_key_default:content_type_default, authorization_key_default:authorization_carrier_default+launch_detail.token_userid_primary}

request_detail = requests_constants()

class workitem_constants:
    witypescenario = "71171e90-6d35-498f-a6a7-2083b5267c18"
    witypefundamental =  "ee7ca005-f81d-4eea-9b9b-1965df0988d0"
    witypepapercut = "6d603ab4-7c5e-4c5f-bba8-a3ba9d370985"
    witypeexperience =   "b9a71831-c803-4f66-8774-4193fffd1311"
    witypevalue =    "3194ab60-855b-4155-9005-9dce4a05f1eb"
    witypefeature =  "0a24d3c2-e0a6-4686-8051-ec0ea1915a28"
    witypebug =  "26787039-b68f-4e28-8814-c2f93be1ef4e"
    witypetask = "bbf35418-04b6-426c-a60b-7f80beb0b624"
    
    wilinktype_parent = "25c326a7-6d03-4f5a-b23b-86a9ee4171e9" ## On Prod
    
    label_1 = "sample_label_1"
    label_2 = "sample_label_2"
    label_3 = "sample_label_3"
    label_4 = "sample_label_4"
    label_5 = "sample_label_5"
    
    iteration_1 = "Iteration_1"
    iteration1_1 = "Iteration1_1"
    iteration_2 = "Iteration_2"
    
    comment_1_text = "Comment # 1"
    comment_2_text = "Comment # 2"


class dynamic_data:
    username = None
    userid = None
    
    spaceid = None
    spacename = None
    spacelink = None
    
    parent_area_id = None
    parent_area_name = None
    area_names_to_ids = {}
    
    parent_iteration_id = None
    parent_iteration_name = None
    iteration_names_to_ids = {}
    nested_iters_names_to_ids = {}
    
    labels_names_to_ids = {}
    
    wi_names_to_ids = {}
    wi_names_to_links = {}

dynamic_vars = dynamic_data()

    
    