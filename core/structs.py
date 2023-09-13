import inspect
from abc import abstractmethod
from collections import OrderedDict
from copy import deepcopy
from threading import Lock


class SingletonMetaBase(type):
    """
    singleton meta base class.

    this is a thread-safe implementation of singleton.
    """

    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        if cls._has_instance() is False:
            with cls._lock:
                if cls._has_instance() is False:
                    instance = super().__call__(*args, **kwargs)
                    cls._register_instance(instance)

        return cls._get_instance()

    @abstractmethod
    def _has_instance(cls):
        """
        gets a value indicating there is a registered instance.

        :raises NotImplementedError: not implemented error.

        :rtype: bool
        """

        raise NotImplementedError()

    @abstractmethod
    def _register_instance(cls, instance):
        """
        registers the given instance.

        :param object instance: instance to be registered.

        :raises NotImplementedError: not implemented error.
        """

        raise NotImplementedError()

    @abstractmethod
    def _get_instance(cls):
        """
        gets the registered instance.

        :raises NotImplementedError: not implemented error.

        :rtype: object
        """

        raise NotImplementedError()


class UniqueSingletonMeta(SingletonMetaBase):
    """
    unique singleton meta class.

    this is a thread-safe implementation of singleton.
    this class only allows a single unique object for all descendant types.

    for example: {Base -> UniqueSingletonMeta, A -> Base, B -> A}
    if some_object = Base() then always Base() = A() = B() = some_object.
    or if some_object = A() then always A() = B() = some_object != Base().
    """

    _instance = None
    _lock = Lock()

    def _has_instance(cls):
        """
        gets a value indicating that there is a registered instance.

        :rtype: bool
        """

        return cls._instance is not None

    def _register_instance(cls, instance):
        """
        registers the given instance.
        """

        cls._instance = instance

    def _get_instance(cls):
        """
        gets the registered instance.

        :rtype: object
        """

        return cls._instance
