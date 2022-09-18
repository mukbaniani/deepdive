    post

    byline (one or more authors)
        author:
            first_name (required, min 2 chars, max 20 chars)
            last_name (required, min 1 char, max 20 chars)
            display_name (optional, default to first name, initial of last name, min 1 char, max 25 chars)
    title (required, at least 10 characters, no more than 50, force title case)
    sub title (optional, if present at least 20 characters, max 100)
    body (required, at least 100 characters, no upper limit)
    links (0 or more)
        link:
            name (required, min 5 characters, max 25 characters)
            url (required, valid url, that must include scheme (http/https))
