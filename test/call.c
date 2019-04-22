#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <curl/curl.h>
#include <curl/easy.h>

//gcc call.c -o call `pkg-config --cflags --libs libcurl`

size_t write_data(void *ptr, size_t size, size_t nmemb, void *stream)
{
    return printf("%s", (char *)ptr);
}

int main(int argc, char *argv[])
{
    CURL *curl;

    curl_global_init(CURL_GLOBAL_ALL);
    curl = curl_easy_init();
    curl_easy_setopt(curl, CURLOPT_URL, argv[1]);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_data);
    curl_easy_perform(curl);
    curl_easy_cleanup(curl);
    exit(0);
}