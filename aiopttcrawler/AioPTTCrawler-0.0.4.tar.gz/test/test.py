from AioPTTCrawler import AioPTTCrawler

def main():
    ptt_crawler = AioPTTCrawler()
    ptt_crawler.get_board_latest_articles("Gossiping", 100)


if __name__ == "__main__":
    main()
