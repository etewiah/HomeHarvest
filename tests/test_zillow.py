from homeharvest import scrape_property


def test_zillow():
    results = [
        scrape_property(
            location="2530 Al Lipscomb Way", site_name="zillow", listing_type="for_sale"
        ),
        scrape_property(
            location="Phoenix, AZ, USA", site_name="zillow", listing_type="for_rent"
        ),
        scrape_property(
            location="Dallas, TX, USA", site_name="zillow", listing_type="sold"
        ),
        scrape_property(location="85281", site_name="zillow"),
    ]

    assert all([result is not None for result in results])