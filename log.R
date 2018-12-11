d <- readr::read_csv("~/.talon/phrase_log.csv",
  col_names = c("phrase", "date", "app"),
  col_types = readr::cols(
    phrase  = readr::col_character(),
    date    = readr::col_datetime(format = ""),
    app     = readr::col_character()
))
