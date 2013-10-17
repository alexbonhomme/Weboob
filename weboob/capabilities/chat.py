# -*- coding: utf-8 -*-

# Copyright(C) 2010-2011 Christophe Benz
#
# This file is part of weboob.
#
# weboob is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# weboob is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with weboob. If not, see <http://www.gnu.org/licenses/>.


import datetime

from .base import IBaseCap, CapBaseObject, StringField, DateField, UserError


__all__ = ['ChatException', 'ChatMessage', 'ICapChat']


class ChatException(UserError):
    """
    Exception raised when there is a problem with the chat.
    """


class ChatMessage(CapBaseObject):
    """
    Message on the chat.
    """
    id_from =       StringField('ID of sender')
    id_to =         StringField('ID of recipient')
    message =       StringField('Content of message')
    date =          DateField('Date when the message has been sent')

    def __init__(self, id_from, id_to, message, date=None):
        CapBaseObject.__init__(self, '%s.%s' % (id_from, id_to))
        self.id_from = id_from
        self.id_to = id_to
        self.message = message
        self.date = date

        if self.date is None:
            self.date = datetime.datetime.utcnow()


class ICapChat(IBaseCap):
    """
    Websites with a chat system.
    """
    def iter_chat_messages(self, _id=None):
        """
        Iter messages.

        :param _id: optional parameter to only get messages
                    from a given contact.
        :type _id: str
        :rtype: iter[:class:`ChatMessage`]
        """
        raise NotImplementedError()

    def send_chat_message(self, _id, message):
        """
        Send a message to a contact.

        :param _id: ID of recipient
        :type _id: str
        :param message: message to send
        :type message: str
        :raises: :class:`ChatException`
        """
        raise NotImplementedError()