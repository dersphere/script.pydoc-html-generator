from pydoc import resolve, html, describe

import xbmcaddon
import xbmcgui
import xbmc


MODULES = ('xbmc', 'xbmcplugin', 'xbmcgui', 'xbmcaddon', 'xbmcvfs')


if (__name__ == "__main__"):
    Addon = xbmcaddon.Addon('script.pydoc-html-generator')
    Dialog = xbmcgui.Dialog()
    getString = Addon.getLocalizedString
    if not Addon.getSetting('save_path'):
        if Dialog.yesno(getString(30001),  # choose folder
                         getString(30002),  # Please choose a folder
                         getString(30005)):  # Do you want to set now?
            Addon.openSettings()
    if Addon.getSetting('save_path'):
        for module_name in MODULES:
            try:
                object, name = resolve(module_name, 0)
                page = html.page(describe(object), html.document(object, name))
                file_path = '%s/%s.html' % (Addon.getSetting('save_path'),
                                            module_name)
                file = open(xbmc.translatePath(file_path), 'w')
                file.write(page)
                file.close()
            except:
                xbmc.log('Unable to save doc for module "%s"' % module_name)
        Dialog.ok(getString(30003),  # Finish
                  getString(30004),  # HTML pydoc's generated in
                  xbmc.translatePath(Addon.getSetting('save_path')))  # path
