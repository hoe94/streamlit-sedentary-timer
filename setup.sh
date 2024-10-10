mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"lkh_bear94@hotmal.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml