import web

urls = (
    '/', 'mvc.controllers.index.Index',
    '/list', 'mvc.controllers.actions.list.Lista',
    '/insert', 'mvc.controllers.actions.insert.Insert',
    '/delete', 'mvc.controllers.actions.delete.Delete',
    '/view', 'mvc.controllers.actions.viewOne.View',
    '/update', 'mvc.controllers.actions.update.Update',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()