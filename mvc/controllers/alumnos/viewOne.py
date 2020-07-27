import web
render=web.template.render('mvc/views/actions/')

class View:
    def GET(self):
        try:
            return render.viewOne()
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result