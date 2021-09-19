def get_query(cursor, is_slim_query=True):
    query_prefixe = "{"

    query_header = get_query_header(cursor)

    qery_metadata = """{
        numberReturned
        pageInfo {
          hasNextPage
          endCursor
          totalCount
        }"""

    query_content = get_query_content(is_slim_query=is_slim_query)

    query_suffixe = "} }"

    return query_prefixe + query_header + qery_metadata + query_content + query_suffixe


def get_query_header(cursor):
    query_header = f'apps(first: 1200, after: "{cursor}")'
    return query_header


def get_query_content(is_slim_query=True):
    if is_slim_query:
        query_content = get_slim_query_content()
    else:
        query_content = get_full_query_content()

    return query_content


def get_slim_query_content():
    query_content = """
        items {
          id          
          title
          developerName          
          publisherName
          type
          osType
          storeIds {
            store
            id
          }
          computedValues {
            earliestReleaseDate
            earliestStreetDate
          }          
        }
        """

    return query_content


def get_full_query_content():
    query_content = """
        items {
          osType
          id
          cmsId
          sortName
          title
          longDescription
          contentRatings {
            type
            categoryKey
          }
          developerName
          geForceUrl
          images {
            FEATURE_IMAGE
            GAME_BOX_ART
            HERO_IMAGE
            MARQUEE_HERO_IMAGE
            ANSEL_360_IMAGES            
            KEY_ART
            KEY_ICON
            KEY_IMAGE
            TV_BANNER
            SCREENSHOTS
            SCREENSHOT_THUMB
          }
          keywords
          maxLocalPlayers
          maxOnlinePlayers
          apks {
            type
            version
            url
          }
          publisherName
          storeIds {
            id
            store
          }
          streamingModes {
            framesPerSecond
            heightInPixels
            widthInPixels
          }
          supportedControls
          supportedGamePlayModes
          type
          computedValues {
            earliestReleaseDate
            earliestStreetDate
            allKeywords
          }
          genres
          appStore
          variants {
            id
            title
            appStore
            developerName
            gfn {
              status
              visibility
              releaseDate
              isInLibrary
            }
            osType
            storeId
          }
        }
        """

    return query_content


def main():
    for is_slim_query in [False, True]:
        query_input = get_query("", is_slim_query=is_slim_query)
        print(query_input)

    return


if __name__ == "__main__":
    main()
