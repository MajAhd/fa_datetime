import pyvalidation.rules as Rules


class BindRules:
    """
     Bind Validation Rules from /rules
     :param rule validate name and the rule of validate
     :param rule_val validate default value ro further process
     :param all_data all data inside the validation request
    """

    def __init__(self, rule, rule_val, all_data):
        self.rule = rule
        self.rule_val = rule_val
        self.all_data = all_data

    def build(self, key, value):
        """
        base on rule bind and run validation
        :param key: data name
        :param value: data value
        :return: Boolean
        """
        match self.rule:
            case "required":
                return Rules.Required(value).is_required()
            case "accepted":
                return Rules.Accepted(value).is_accepted()
            case "boolean":
                return Rules.Boolean(value).is_boolean()
            case "confirmed":
                confirmed_name = f"{key}_confirmation"
                if Rules.Field(self.all_data, confirmed_name).field_exist():
                    target = self.all_data[confirmed_name]
                    return Rules.Confirmation(value, target)
                return False
            # Date Time Validation
            case "date":
                return Rules.DateTime(value).is_date()
            case "time":
                return Rules.DateTime(value).is_time()
            case "datetime":
                return Rules.DateTime(value).is_date_time()
            case "timezone":
                return Rules.DateTime(value).is_timezone()
            case "date_equals":
                if Rules.DateTime(self.rule_val).is_date():
                    return Rules.DateTime(value).date_equals(self.rule_val)
                return False
            case "after":
                if Rules.DateTime(self.rule_val).is_date():
                    return Rules.DateTime(value).is_after(self.rule_val)
                return False
            case "after_or_equal":
                if Rules.DateTime(self.rule_val).is_date():
                    return Rules.DateTime(value).is_after_or_equal(self.rule_val)
                return False
            case "before":
                if Rules.DateTime(self.rule_val).is_date():
                    return Rules.DateTime(value).is_before(self.rule_val)
                return False
            case "before_or_equal":
                if Rules.DateTime(self.rule_val).is_date():
                    return Rules.DateTime(value).is_before_or_equal(self.rule_val)
                return False
            # different Validation
            case "different":
                return Rules.Different(value).is_different(self.rule_val)
            case "equal":
                return Rules.Different(value).is_equal(self.rule_val)
            case "gt":
                return Rules.Different(value).gt(self.rule_val)
            case "gte":
                return Rules.Different(value).gte(self.rule_val)
            case "lt":
                return Rules.Different(value).lt(self.rule_val)
            case "lte":
                return Rules.Different(value).lte(self.rule_val)
            # Inside
            case "in":
                return Rules.Inside(value).is_in(self.rule_val)
            case "not_in":
                return Rules.Inside(value).is_not_in(self.rule_val)
            # Internet
            case "email":
                return Rules.Internet(value).email()
            case "url":
                return Rules.Internet(value).url()
            case "ip":
                return Rules.Internet(value).ip()
            case "ipv4":
                return Rules.Internet(value).ipv4()
            case "ipv6":
                return Rules.Internet(value).ipv6()
            case _:
                return "Validation Not Defined!"
