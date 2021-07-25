
import csv


class Read:
    def read_member(self,file):
        member = []
        with open(file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=",", lineterminator="\n")

            for row in csv_reader:

                r = row["username"]
                member.append(r)

        return member

    def read_group(self,file):
        group = []
        with open(file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=",", lineterminator="\n")

            for row in csv_reader:

                r = row["link"]
                group.append(r)
        return group
