d <- read.csv("~/.talon/phrase_log.csv",
  col.names = c("phrase", "date", "app"),
  stringsAsFactors = FALSE, strip.white = TRUE)
d$date <- lubridate::ymd_hms(d$date)

library(dplyr)
d %>%
  group_by(phrase) %>%
  summarize(n = n()) %>%
  arrange(-n) %>%
  top_n(10)

d <- d %>% mutate(time_difference = c(NA, date[-1] - date[-length(date)])) %>%
  mutate(short_difference = time_difference < 3) %>%
  group_by(app)
head(d)
