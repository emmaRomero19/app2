import web
render=web.template.render('mvc/views/actions/')

class Lista:
    def GET(self):
        try:
            return render.list()
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result