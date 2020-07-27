import web
render=web.template.render('mvc/views/alumnos/')

class Insert:
    def GET(self):
        try:
            return render.insert()
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result