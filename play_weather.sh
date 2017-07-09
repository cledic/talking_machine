./play_speech.sh "$(cat /tmp/curr_weather.txt)"
sleep 2
./play_speech.sh "$(cat /tmp/today_weather.txt)"
sleep 2
./play_speech.sh "$(cat /tmp/tomorrow_weather.txt)"
sleep 2
./play_speech.sh "$(cat /tmp/twodayslater_weather.txt)"
