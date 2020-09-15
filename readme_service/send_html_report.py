from jinja2 import *
import jinja2

def file_operation(template_name,data_json,user_data):
    '''context manager for templating'''
    try:
        data_json["UserName"] = user_data
        with ContextManager(template_name,'r') as infile: #, ContextManager(exep,'w') as outfile:
                render = Template(infile.read()).render(data_json)
                return render
    except (IOError,TemplateSyntaxError,jinja2.exceptions.UndefinedError) as error:
        print ("getting error in jinja {}".format(error))
        #raise

class ContextManager(object):
    '''file handling func'''
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        try:
            self.file = open(self.filename,self.mode);return self.file
        except IOError as e:
            logging.error("Error code --> [%s]" % (e),100, ex=True)

    def __exit__(self,exc_type, exc_value, exc_traceback):
        self.file.close()

