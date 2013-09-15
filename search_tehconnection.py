import logging
from flexget.entry import Entry
from flexget.plugin import register_plugin
from flexget.utils.tools import urlopener
from flexget.utils.soup import get_soup
from flexget.utils.search import torrent_availability

log = logging.getLogger('search_tehconnection')

class SearchTC(object):
	def search(self, entry, config):
		url = "https://tehconnection.eu/torrents.php?searchstr=%s" \
			% entry.get("imdb_id")

		page = urlopener(url, log)
		soup = get_soup(page)

		results = set()

		for row in soup.find_all("tr", class_="group_torrent"):
			link = row.find(title="Download")
			info = row.find(colspan="1").contents[3].contents[0].strip()
			seeders = int(row.find_all("td")[6].contents[0].strip())
			leechers = int(row.find_all("td")[7].contents[0].strip())

			result = Entry()
			result["title"] = entry.get("title") + " / " + info
			result["imdb_id"] = entry.get("imdb_id");
			result["url"] = "https://tehconnection.eu" + link.get("href")
			result["torrent_seeds"] = seeders
			result["torrent_leeches"] = leechers
			result["search_sort"] = torrent_availability(result['torrent_seeds'],
																									 result['torrent_leeches'])

			results.add(result)

		return results

register_plugin(SearchTC, 'search_tehconnection', groups=['search'], debug=True)
