
class AuthRouter:
    route_app_labels = {'auth', 'contenttypes', 'admin', 'sessions'}

    def db_for_read(self,model,**hints): # Grant read access
        if model._meta.app_label in self.route_app_labels: # If app_label of model is one of the route_app_labels defined
                                                            # defined above
            return 'auth_db' # Return user_db database
        return None

    def db_for_write(self,model,**hints): # Grant write access
        if model._meta.app_label in self.route_app_labels: # If app_label of model is one of the route_app_labels defined
                                                            # defined above
            return 'auth_db' # Return user_db database
        return None
        
    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'auth_db'
        return None

class Blue:
    route_app_labels = {'blue',}

    def db_for_read(self,model,**hints): # Grant read access
        if model._meta.app_label in self.route_app_labels: # If app_label of model is one of the route_app_labels defined
                                                            # defined above
            return 'blue_db' # Return user_db database
        return None

    def db_for_write(self,model,**hints): # Grant write access
        if model._meta.app_label in self.route_app_labels: # If app_label of model is one of the route_app_labels defined
                                                            # defined above
            return 'blue_db' # Return user_db database
        return None
        
    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'blue_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'blue_db'
        return None

        