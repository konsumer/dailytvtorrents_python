# library to get data from dailytvtorrents.org
# http://api.dailytvtorrents.org/

import json, urllib, urllib2


class DailyTvTorrents():
    version = "1.0"
    
    def __getattr__(self, name):
        def q(**arguments):
            try:
                del arguments['jsonp']
            except KeyError:
                pass
            url = 'http://api.dailytvtorrents.org/%s/%s?%s' % (self.version, name.replace("_","."), urllib.urlencode(arguments))
            
            try:
                out = urllib2.urlopen(url)
            except urllib2.HTTPError as e:
                if e.code == 400:
                    e.msg = "badly formatted request"
                elif e.code == 404:
                    e.msg = "the query you asked for did not return any data"
                elif e.code == 503:
                    e.msg = "your available credits ran out (reset every 24 hours)"
                raise e

            if out.headers['Content-type'] == "application/json":
                return json.load(out)
            else:
                return out.read()
        return q

# testing / examples
if __name__ == "__main__":
    d = DailyTvTorrents()
    
    print d.episode_getLatest(show_name="futurama")

    print d.misc_getCleanFileName(filename="futurama.6x15.some.title.avi")
    print d.misc_getCleanFileName(filename="The_Colbert_Report_2011_06_06.avi")
    print d.misc_getCleanFileName(filename="Star_Wars._The_Clone_Wars_3x20x21x22.mp4")
    print d.misc_getCleanFileName(filename="_The_Playboy_Club_S01E01_720p_HDTV_X264-DIMENSION.mkv")
    print d.misc_getCleanFileName(filename="example.s1e1")
    print d.misc_getCleanFileName(filename="dtt-can't-parse-this")

    print d.show_getEpisodes(show_name="futurama")

    print d.show_getInfo(show_name="futurama")

    #print d.shows_getNew()
    #print d.shows_getNew(strict="yes")
    #print d.shows_getNew(strict="yes", max_age_hours=168)

    print d.shows_getPopular()
    print d.shows_getPopular(max_items=3)

    print d.shows_getReturning()
    print d.shows_getReturning(max_items=2)

    print d.shows_getTextInfo(show_names="futurama,breaking-bad,weeds,terra-nova", links="yes")

    print d.shows_search(query="fut ur ama")
    print d.shows_search(query="america", page=2)
    print d.shows_search(query="america most")

    print d.torrent_getInfo(show_name="futurama", episode_num="S06E23", quality=720)

    print d.torrent_getInfos(show_name="futurama", episode_num="S06E23")

    print d.torrent_getInfosAll(show_name="futurama", episode_num="S06E23")

    print d.torrent_getLatest(show_name="futurama", quality=720)

    
    
    
    