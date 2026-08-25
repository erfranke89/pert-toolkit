import re
import unittest
from pathlib import Path


HTML = (Path(__file__).parents[1] / "index.html").read_text()


class SiteSmokeTests(unittest.TestCase):
    def test_mobile_zoom_is_available(self):
        viewport = re.search(r'<meta name="viewport" content="([^"]+)"', HTML).group(1)
        self.assertNotIn("maximum-scale", viewport)
        self.assertNotIn("user-scalable=no", viewport)

    def test_all_sections_have_jump_targets(self):
        tabs = set(re.findall(r"showTab\('([^']+)'", HTML))
        options = set(re.findall(r'<option value="([^"]+)"', HTML))
        self.assertTrue(tabs.issubset(options))
        for tab in tabs:
            self.assertIn(f'id="{tab}"', HTML)

    def test_direct_section_links_are_supported(self):
        self.assertIn('aria-current', HTML)
        self.assertIn('location.hash.slice(1)', HTML)


if __name__ == "__main__":
    unittest.main()
