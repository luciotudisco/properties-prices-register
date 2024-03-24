/* eslint-disable @typescript-eslint/no-explicit-any */

import Moment from "moment";
import SearchHitClips from "./HitClips";
import { Card, Flex, NavLink, NumberFormatter, Text } from "@mantine/core";
import { IconBrandGoogleMaps } from "@tabler/icons-react";

const Hit = function (props: { hit: any }): JSX.Element {
  const { hit } = props;
  return (
    <Card padding="sm" withBorder radius={0}>
      <Flex className="w-full flex-col gap-2">
        <Flex className="w-full flex-col md:flex-row md:justify-between gap-2">
          <Flex className="flex flex-col gap-2">
            <Flex className="flex w-full flex-row gap-2 items-center">
              <Text className="text-zinc-900 text-nowrap" size="xs">
                {hit.raw_address}
              </Text>
              <NavLink
                aria-label="Open Google Maps Link"
                className="text-xs p-0 font-extralight bg-transparent"
                leftSection={<IconBrandGoogleMaps size={16} />}
                variant="light"
                href={`http://maps.google.com/maps?z=12&t=m&q=loc:${hit.latitude}+${hit.longitude}`}
                target="_blank"
                hidden={hit.location_type !== "exact"}
                active
              />
            </Flex>
            <Text className="text-zinc-500" size="xs">
              {Moment(hit.sale_date * 1000).format("ll")}
            </Text>
          </Flex>
          <NumberFormatter
            value={hit.price}
            thousandSeparator={true}
            className="text-zinc-900 font-bold flex items-center text-xs"
            prefix="€"
          />
        </Flex>
        <SearchHitClips hit={hit} />
      </Flex>
    </Card>
  );
};

export default Hit;
