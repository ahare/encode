#ffmpeg -y -i samples/contrasts.flv -ar 22050 -ab 64k -ac 1 -crf 30 -g 150 -pix_fmt yuvj420p output/washed.mp4

#ffmpeg -y -i samples/contrasts.flv -ar 22050 -ab 64k -ac 1 -crf 30 -g 150 output/pink.mp4

ffmpeg -y -i samples/contrasts.flv -ar 22050 -ab 64k -ac 1 output/nopts.mp4
