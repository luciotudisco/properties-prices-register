/* eslint-disable @typescript-eslint/no-explicit-any */

import Moment from "moment";
import SearchHitClips from "./HitClips";
import Link from "next/link";
import { Grid, Group, NavLink, NumberFormatter, Text } from "@mantine/core";
import { IconBrandGoogleMaps } from "@tabler/icons-react";

const SearchHit = function (props: { hit: any }): JSX.Element {
  const { hit } = props;
  return (
    <Grid className="w-full h-full">
      <Grid.Col
        span={{ base: 12, md: 8 }}
        className="flex flex-col w-full h-full gap-2"
      >
        <Group gap="xs">
          <Text className="text-zinc-900" size="sm">
            {hit.raw_address}
          </Text>
          <Link
            href={`http://maps.google.com/maps?z=12&t=m&q=loc:${hit.latitude}+${hit.longitude}`}
            target="_blank"
            hidden={hit.location_type !== "exact"}
          >
            <NavLink
              aria-label="Open Google Maps Link"
              className="text-xs p-0 font-extralight bg-transparent"
              leftSection={<IconBrandGoogleMaps />}
              variant="light"
              active
            />
          </Link>
        </Group>
        <Text className="text-zinc-500" size="xs">
          {Moment(hit.sale_date * 1000).format("ll")}
        </Text>
      </Grid.Col>
      <Grid.Col
        span={{ base: 12, md: 4 }}
        className="flex flex-col h-full gap-2 md:items-end sm:items-start align-middle justify-center"
      >
        <NumberFormatter
          value={hit.price}
          thousandSeparator={true}
          className="text-zinc-900 font-bold"
          prefix="€"
        />
      </Grid.Col>
      <Grid.Col span={{ base: 12 }}>
        <SearchHitClips hit={hit} />
      </Grid.Col>
    </Grid>
  );
};

export default SearchHit;
