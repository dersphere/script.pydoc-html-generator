from pydoc import resolve, html, describe

import xbmcaddon
import xbmcgui
import xbmc


MODULES = ('xbmc', 'xbmcplugin', 'xbmcgui', 'xbmcaddon', 'xbmcvfs')


if (__name__ == "__main__"):
    Addon = xbmcaddon.Addon('script.pydoc-html-generator')
    Dialog = xbmcgui.Dialog()
    getString = Addon.getLocalizedString
    while Addon.getSetting('save_path') == '':
        Dialog.ok(getString(30001),  # choose folder
                  getString(30002))  # Please choose a folder
        Addon.openSettings()
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
            xbmc.log('Could not generate doc for module "%s"' % module_name)
    Dialog.ok(getString(30003),  # Finish
              getString(30004),  # HTML pydoc's generated in
              xbmc.translatePath(Addon.getSetting('save_path')))  # path
