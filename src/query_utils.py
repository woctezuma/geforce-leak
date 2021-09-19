def get_query(cursor, is_slim_query=True, use_original_endpoint=True):
    query_prefixe = "{"

    query_header = get_query_header(cursor, use_original_endpoint=use_original_endpoint)

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


def get_header_sep():
    return ", "


def get_query_header(cursor, use_original_endpoint=True, app_ids=None):
    if app_ids is None:
        app_ids = []

    if len(app_ids) > 0:
        line_sep = "\n"
        app_ids_stack = line_sep.join(f'"{id}"' for id in app_ids)
        app_ids_str = f"appIds: [ {app_ids_stack} ]" + get_header_sep()
    else:
        app_ids_str = ""

    if use_original_endpoint:
        vpc_id = ""
    else:
        vpc_id = 'vpcId: "NP-SEA-01"' + get_header_sep()

    query_header = f'apps({app_ids_str}{vpc_id}first: 1200, after: "{cursor}")'
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
        query_input = get_query(
            "", is_slim_query=is_slim_query, use_original_endpoint=False
        )
        print(query_input)

    return


if __name__ == "__main__":
    main()
