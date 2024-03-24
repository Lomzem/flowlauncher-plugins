from flowlauncher import FlowLauncher


class ShareCalc(FlowLauncher):
    def query(self, query):
        account_value = 0
        with open("account_value.txt", "r") as f:
            account_value = float(f.read()) / 2

        return [
            {
                "title": "",
                # "subTitle": f"{float(query) / account_value}",
                "subTitle": f"{repr(query)}",
                "icoPath": "Images/calculator.png",  # related path to the image
                "score": 0,
            }
        ]


if __name__ == "__main__":
    ShareCalc()
