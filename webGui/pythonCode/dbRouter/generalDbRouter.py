
class GeneralDbRouter:
    customRoutes = {"world": "player_data",
                    }

    def db_for_read(self, model, **hints):
        if model._meta.db_table in self.customRoutes:
            return self.customRoutes[model._meta.db_table]
        else:
            return "default"

    def db_for_write(self, model, **hints):
        """
        Writes always go to primary.
        """
        return "default"