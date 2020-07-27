import web
render=web.template.render('mvc/views/alumnos/')

class Update:
    def GET(self):
        try:
            return render.update()
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result