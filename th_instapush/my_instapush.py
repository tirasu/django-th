# coding: utf-8
from instapush import Instapush, App

# django classes
from django.utils.log import getLogger

# django_th classes
from django_th.services.services import ServicesMgr
from th_instapush.models import Instapush as InstapushModel

"""
    handle process with instapush
    put the following in settings.py

    TH_SERVICES = (
        ...
        'th_instapush.my_instapush.ServiceInstapush',
        ...
    )
"""

logger = getLogger('django_th.trigger_happy')


class ServiceInstapush(ServicesMgr):

    def __init__(self, token=None, **kwargs):
        super(ServiceInstapush, self).__init__(token, **kwargs)
        self.token = token

    def read_data(self, **kwargs):
        """
            get the data from the service
            as the pocket service does not have any date
            in its API linked to the note,
            add the triggered date to the dict data
            thus the service will be triggered when data will be found

            :param kwargs: contain keyword args : trigger_id at least
            :type kwargs: dict

            :rtype: list
        """
        pass

    def save_data(self, trigger_id, **data):
        """
            let's save the data

            :param trigger_id: trigger ID from which to save data
            :param data: the data to check to be used and save
            :type trigger_id: int
            :type data:  dict
            :return: the status of the save statement
            :rtype: boolean
        """
        title, content = super(ServiceInstapush, self).save_data(trigger_id,
                                                                 **data)
        instance = InstapushModel.objects.get(trigger_id=trigger_id)
        Instapush(user_token=self.token)
        app = App(appid=instance.app_id, secret=instance.app_secret)
        trackers = {instance.tracker_name: content}
        status = app.notify(event_name=instance.event_name,
                            trackers=trackers)
        return status
