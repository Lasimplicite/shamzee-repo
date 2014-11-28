import xbmcaddon
import util

addon = xbmcaddon.Addon('plugin.video.silverbirdtv')

util.playMedia(addon.getAddonInfo('name'), addon.getAddonInfo('icon'), 
               'http://iphone-streaming.ustream.tv/uhls/18482308/streams/live/iphone/playlist.m3u8')