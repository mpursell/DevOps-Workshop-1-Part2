import argparse



def add_Review():

    parser = argparse.ArgumentParser()

    parser.add_argument('--film')
    parser.add_argument('--stars')

    args = parser.parse_args()

    filmName = args.film
    rating = args.stars

    with open('films.csv', 'a') as csv:

        string = filmName + ',' + rating
        csv.write(string + '\n')


if __name__ == "__main__":


    add_Review()



