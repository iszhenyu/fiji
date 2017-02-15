# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/1/5 下午2:17
"""
from app.extensions import db


class Service(object):
    """
    A :class:`Service` instance encapsulates common SQLAlchemy model
    operations in the context of a :class:`Flask` application.
    """
    __model__ = None

    def _isinstance(self, model, raise_error=True):
        """
        Checks if the specified model instance matches the service's model.
        By default this method will raise a `ValueError` if the model is not the
        expected type.
        """
        rv = isinstance(model, self.__model__)
        if not rv and raise_error:
            raise ValueError('%s is not of type %s' % (model, self.__model__))
        return rv

    def _preprocess_params(self, kwargs):
        """
        Returns a preprocessed dictionary of parameters. Used by default
        before creating a new instance or updating an existing instance.
        """
        kwargs.pop('csrf_token', None)
        return kwargs

    def new_instance(self, **kwargs):
        """
        返回对应模型的实例,未保存
        """
        return self.__model__(**self._preprocess_params(kwargs))

    def save(self, model):
        """
        Commits the model to the database and returns the model
        """
        self._isinstance(model)
        db.session.add(model)
        db.session.commit()
        return model

    def update(self, model, **kwargs):
        """
        Returns an updated instance of the service's model class.
        """
        self._isinstance(model)
        for k, v in self._preprocess_params(kwargs).items():
            setattr(model, k, v)
        self.save(model)
        return model

    def delete(self, model):
        """
        Immediately deletes the specified model instance.
        """
        self._isinstance(model)
        db.session.delete(model)
        db.session.commit()

    def first(self, **kwargs):
        """
        Returns the first instance found of the service's model filtered by
        the specified key word arguments.
        """
        return self.list_by_params(**kwargs).first()

    def all(self):
        """
        Returns a generator containing all instances of the service's model.
        """
        return self.__model__.query.all()

    def get_by_id(self, id):
        """
        Returns an instance of the service's model with the specified id.
        Returns `None` if an instance with the specified id does not exist.
        """
        return self.__model__.query.get(id)

    def list_by_ids(self, *ids):
        """
        Returns a list of instances of the service's model with the specified ids.
        """
        return self.__model__.query.filter(self.__model__.id.in_(ids)).all()

    def list_by_params(self, **kwargs):
        """
        Returns a list of instances of the service's model filtered by the
        specified key word arguments.
        """
        return self.__model__.query.filter_by(**kwargs)
