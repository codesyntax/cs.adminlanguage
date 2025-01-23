from Acquisition import aq_inner
from cs.adminlanguage.negotiator import get_editor_language
from cs.adminlanguage.negotiator import logger
from plone.app.layout.globals.portal import PortalState as PortalStateBase


class PortalState(PortalStateBase):

    def language(self):
        try:
            language = get_editor_language(self.request)
            if language:
                return language
        except Exception as e:
            # Some defensive programming here
            logger.error("Admin language force patch failed")
            logger.exception(e)

        return (
            self.request.get("LANGUAGE", None)
            or aq_inner(self.context).Language()
            or self.default_language()
        )
