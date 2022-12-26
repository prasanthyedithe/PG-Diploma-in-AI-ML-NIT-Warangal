import logging as log


def print_all_feeds(entry):
    log.info("In print_all_feeds(entry) with Input values :" + str(entry))
    for item in entry:
        # print("keys : ", item.keys())
        print("title : ", item.title)
        print("title_detail : ", item.title_detail)
        print("links : ", item.links)
        print("link : ", item.link)
        print("published : ", item.published)
        print("published_parsed : ", item.published_parsed)
        print("source : ", item.source)
        print("id : ", item.id)
        print("guidislink : ", item.guidislink)
        print("media_content : ", item.media_content)
        print("media_credit : ", item.media_credit)
        print("credit : ", item.credit)


def print_range_feeds(entry, limit_value):
    log.info("In print_range_feeds(entry, limit_value) with Input values :" + str(entry), limit_value)
    for item in range(0, limit_value):
        print("title : ", entry[item].title)
        print("title_detail : ", entry[item].title_detail)
        print("links : ", entry[item].links)
        print("link : ", entry[item].link)
        print("published : ", entry[item].published)
        print("published_parsed : ", entry[item].published_parsed)
        print("source : ", entry[item].source)
        print("id : ", entry[item].id)
        print("guidislink : ", entry[item].guidislink)
        print("media_content : ", entry[item].media_content)
        print("media_credit : ", entry[item].media_credit)
        print("credit : ", entry[item].credit)


def construct_json_all_feeds(entry, my_json_list):
    log.info("In construct_json_all_feeds(entry, my_json_list) with Input values :" + str(entry), str(my_json_list))
    for item in entry:
        json_object = {"title": item.title, "title_detail": item.title_detail, "links": item.links,
                       "link": item.link, "published": item.published, "published_parsed": item.published_parsed,
                       "source": item.source, "id": item.id, "guidislink": item.guidislink,
                       "media_content": item.media_content, "media_credit": item.media_credit,
                       "credit": item.credit}
        my_json_list.append(json_object)
    return my_json_list


def construct_json_range_feeds(entry, limit_value, my_json_list):
    log.info("In construct_json_range_feeds(entry, limit_value, my_json_list) with Input values :" + str(entry),
             limit_value,
             str(my_json_list))
    for item in range(0, limit_value):
        json_object = {"title": entry[item].title, "title_detail": entry[item].title_detail,
                       "links": entry[item].links,
                       "link": entry[item].link, "published": entry[item].published,
                       "published_parsed": entry[item].published_parsed,
                       "source": entry[item].source, "id": entry[item].id, "guidislink": entry[item].guidislink,
                       "media_content": entry[item].media_content, "media_credit": entry[item].media_credit,
                       "credit": entry[item].credit}
        my_json_list.append(json_object)
    return my_json_list
