import web
render=web.template.render('mvc/views/actions/')

class Delete:
    def GET(self):
        try:
            return render.delete()
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result