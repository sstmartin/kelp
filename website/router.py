class WebsiteRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'website':
            return 'yelp_data'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'website':
            return 'yelp_data'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'website' and obj2._meta.app_label == 'website':
            return True
        elif 'website' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_syncdb(self, db, model):
        if db == 'yelp_data' or model._meat.app_label == 'website':
            return False
        else:
            return True